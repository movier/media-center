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
  },
});

export const { saveVideoListData } = videoSlice.actions;

export default videoSlice.reducer;
export const selectVideoList = state => state.video.list;
