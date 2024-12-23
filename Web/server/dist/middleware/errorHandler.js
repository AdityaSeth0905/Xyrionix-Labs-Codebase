"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.createError = exports.ErrorType = exports.catchAsync = exports.errorHandler = exports.AppError = void 0;
class AppError extends Error {
    statusCode;
    status;
    isOperational;
    constructor(message, statusCode = 500, isOperational = true) {
        super(message);
        Object.setPrototypeOf(this, AppError.prototype);
        this.name = this.constructor.name;
        this.statusCode = statusCode;
        this.status = this.determineStatus(statusCode);
        this.isOperational = isOperational;
        Error.captureStackTrace(this, this.constructor);
    }
    determineStatus(statusCode) {
        if (statusCode >= 400 && statusCode < 500)
            return 'fail';
        if (statusCode >= 500)
            return 'error';
        return 'unknown';
    }
}
exports.AppError = AppError;
const errorHandler = (err, _req, res, _next) => {
    const isAppError = err instanceof AppError;
    const statusCode = isAppError
        ? err.statusCode
        : 500;
    const status = isAppError
        ? err.status
        : 'error';
    if (!isAppError || !err.isOperational) {
        console.error('🔴 UNHANDLED ERROR:', {
            name: err.name,
            message: err.message,
            stack: err.stack
        });
    }
    const responseObject = {
        status,
        message: err.message
    };
    if (process.env.NODE_ENV === 'development') {
        responseObject.stack = err.stack;
    }
    res.status(statusCode).json(responseObject);
};
exports.errorHandler = errorHandler;
const catchAsync = (fn) => {
    return (req, res, next) => {
        fn(req, res, next).catch(next);
    };
};
exports.catchAsync = catchAsync;
var ErrorType;
(function (ErrorType) {
    ErrorType["ValidationError"] = "ValidationError";
    ErrorType["CastError"] = "CastError";
    ErrorType["DuplicateKeyError"] = "DuplicateKeyError";
    ErrorType["AuthenticationError"] = "AuthenticationError";
})(ErrorType || (exports.ErrorType = ErrorType = {}));
const createError = (type, message, statusCode = 400) => {
    const error = new AppError(message, statusCode);
    error.name = type;
    return error;
};
exports.createError = createError;
//# sourceMappingURL=errorHandler.js.map