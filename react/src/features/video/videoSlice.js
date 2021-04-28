import { createSlice } from '@reduxjs/toolkit';

export const videoSlice = createSlice({
  name: 'video',
  initialState: {
    list: [],
  },
  reducers: {
    saveVideoListData: (state, action) => {
      state.list = action.payload;
    },
    removeVideo: (state, action) => {
      state.list = state.list.filter(f => f.id !== parseInt(action.payload));
    }
  },
});

export const { saveVideoListData, removeVideo } = videoSlice.actions;

export default videoSlice.reducer;
export const selectVideoList = state => state.video.list;
