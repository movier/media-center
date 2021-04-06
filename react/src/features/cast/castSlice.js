import { createSlice } from '@reduxjs/toolkit';

export const castSlice = createSlice({
  name: 'cast',
  initialState: {
    list: [],
  },
  reducers: {
    saveCastListData: (state, action) => {
      state.list = action.payload;
    },
  },
});

export const { saveCastListData } = castSlice.actions;
export const selectCastList = state => state.cast.list;
export default castSlice.reducer;
