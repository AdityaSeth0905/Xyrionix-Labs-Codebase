import { Request, Response, NextFunction } from 'express';
declare class AppError extends Error {
    statusCode: number;
    status: string;
    isOperational: boolean;
    constructor(message: string, statusCode?: number, isOperational?: boolean);
    private determineStatus;
}
declare const errorHandler: (err: Error | AppError, _req: Request, res: Response, _next: NextFunction) => void;
declare const catchAsync: <T extends (req: Request, res: Response, _next: NextFunction) => Promise<void>>(fn: T) => (req: Request, res: Response, next: NextFunction) => void;
declare enum ErrorType {
    ValidationError = "ValidationError",
    CastError = "CastError",
    DuplicateKeyError = "DuplicateKeyError",
    AuthenticationError = "AuthenticationError"
}
declare const createError: (type: ErrorType, message: string, statusCode?: number) => AppError;
export { AppError, errorHandler, catchAsync, ErrorType, createError };
