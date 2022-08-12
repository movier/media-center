import { createSlice } from '@reduxjs/toolkit';
import { mediaListGroupByDate } from '../../Utils';

export const videoSlice = createSlice({
  name: 'video',
  initialState: {
    list: [],
  },
  reducers: {
    saveVideoListData: (state, action) => {
      const { payload: originalData } = action;
      state.list = originalData;
    },
    removeVideo: (state, action) => {
      state.list = state.list.filter(f => f.id !== parseInt(action.payload));
    }
  },
});

export const { saveVideoListData, removeVideo } = videoSlice.actions;

export default videoSlice.reducer;
export const selectVideoList = state => mediaListGroupByDate([...state.video.list]);
