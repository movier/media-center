import { createSlice } from '@reduxjs/toolkit';

export const videoSlice = createSlice({
  name: 'video',
  initialState: {
    list: [],
  },
  reducers: {
    saveVideoListData: (state, action) => {
      const { payload: originalData } = action;
      console.log('original data', originalData);
      const basicHeight = 250;
      const windowWidth = window.innerWidth;
      const newData = originalData.slice();
      let rowStartAt = 0;
      let rowEndAt = newData.length - 1;
      let rowWidth = 0;
      let totalRatio = 0;
      for (let index = 0; index < newData.length; index++) {
        const element = newData[index];
        const ratio = element.width / element.height;
        totalRatio += ratio;
        const width = element.width / element.height * basicHeight;
        rowWidth += width;
        if (rowWidth >= windowWidth) {
          // Calculate actual height
          const height1 = windowWidth / (totalRatio - ratio);
          const height2 = windowWidth / totalRatio;
          console.log('height1', index, height1, height2, totalRatio);
          const diff1 = height1 - basicHeight;
          const diff2 = basicHeight - height2;
          if (Math.abs(diff1) > Math.abs(diff2)) {
            rowEndAt = index;
            for (let index1 = rowStartAt; index1 <= rowEndAt; index1++) {
              newData[index1].display_height = height2;
              newData[index1].display_width = newData[index1].width / newData[index1].height * height2
            }
            rowStartAt = index + 1;
            rowWidth = 0;
            totalRatio = 0;
          } else {
            rowEndAt = index - 1;
            for (let index1 = rowStartAt; index1 <= rowEndAt; index1++) {
              newData[index1].display_height = height1;
              newData[index1].display_width = newData[index1].width / newData[index1].height * height1
            }
            rowStartAt = index;
            rowWidth = width;
            totalRatio = ratio;
          }
        }
      }
      console.log('new data 1', newData);
      state.list = newData;
    },
    removeVideo: (state, action) => {
      state.list = state.list.filter(f => f.id !== parseInt(action.payload));
    }
  },
});

export const { saveVideoListData, removeVideo } = videoSlice.actions;

export default videoSlice.reducer;
export const selectVideoList = state => state.video.list;
