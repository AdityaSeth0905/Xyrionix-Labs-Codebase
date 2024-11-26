import { Request, Response, NextFunction } from 'express';

class AppError extends Error {
  statusCode: number;
  status: string;
  isOperational: boolean;

  constructor(
    message: string, 
    statusCode: number = 500, 
    isOperational: boolean = true
  ) {
    super(message);
    
    Object.setPrototypeOf(this, AppError.prototype);

    this.name = this.constructor.name;
    this.statusCode = statusCode;
    this.status = this.determineStatus(statusCode);
    this.isOperational = isOperational;

    Error.captureStackTrace(this, this.constructor);
  }

  private determineStatus(statusCode: number): string {
    if (statusCode >= 400 && statusCode < 500) return 'fail';
    if (statusCode >= 500) return 'error';
    return 'unknown';
  }
}

// Updated error handler to use underscore for unused parameters
const errorHandler = (
  err: Error | AppError, 
  _req: Request,  // Use underscore to indicate intentionally unused
  res: Response, 
  _next: NextFunction  // Use underscore to indicate intentionally unused
) => {
  // Type guard to check if error is an AppError
  const isAppError = err instanceof AppError;

  // Default to 500 internal server error if not an AppError
  const statusCode = isAppError 
    ? (err as AppError).statusCode 
    : 500;

  const status = isAppError 
    ? (err as AppError).status 
    : 'error';

  // Logging for non-operational errors
  if (!isAppError || !(err as AppError).isOperational) {
    console.error('🔴 UNHANDLED ERROR:', {
      name: err.name,
      message: err.message,
      stack: err.stack
    });
  }

  // Response object
  const responseObject: {
    status: string;
    message: string;
    stack?: string;
  } = {
    status,
    message: err.message
  };

  // Add stack trace only in development
  if (process.env.NODE_ENV === 'development') {
    responseObject.stack = err.stack;
  }

  // Send error response
  res.status(statusCode).json(responseObject);
};

// Utility function for async error handling
const catchAsync = <T extends (req: Request, res: Response, _next: NextFunction) => Promise<void>>(
  fn: T
) => {
  return (req: Request, res: Response, next: NextFunction) => {
    fn(req, res, next).catch(next);
  };
};

// Error Types
enum ErrorType {
  ValidationError = 'ValidationError',
  CastError = 'CastError',
  DuplicateKeyError = 'DuplicateKeyError',
  AuthenticationError = 'AuthenticationError'
}

// Factory method for creating specific error types
const createError = (
  type: ErrorType, 
  message: string, 
  statusCode: number = 400
): AppError => {
  const error = new AppError(message, statusCode);
  error.name = type;
  return error;
};

export { 
  AppError, 
  errorHandler, 
  catchAsync, 
  ErrorType, 
  createError 
};