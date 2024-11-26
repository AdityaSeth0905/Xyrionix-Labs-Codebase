declare namespace NodeJS {
    interface ProcessEnv {
      PORT?: string;
      CORS_ORIGIN?: string;
      NODE_ENV?: 'development' | 'production' | 'test';
    }
  }