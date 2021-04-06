import { createSlice } from '@reduxjs/toolkit';

export const videoSlice = createSlice({
  name: 'video',
  initialState: {
    list: [],
  },
  reducers: {
    saveListData: (state, action) => {
      state.list = action.payload;
    },
  },
});

export const { saveListData } = videoSlice.actions;

export default videoSlice.reducer;
export const selectList = state => state.video.list;
