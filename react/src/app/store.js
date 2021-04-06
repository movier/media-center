import { configureStore } from '@reduxjs/toolkit';
import counterReducer from '../features/video/videoSlice';

export default configureStore({
  reducer: {
    video: counterReducer,
  }
});
