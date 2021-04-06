import { configureStore } from '@reduxjs/toolkit';
import videoReducer from '../features/video/videoSlice';
import castReducer from '../features/cast/castSlice';

export default configureStore({
  reducer: {
    video: videoReducer,
    cast: castReducer,
  }
});
