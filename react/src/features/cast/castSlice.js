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
    removeVideoFromPeople: (state, action) => {
      for (let index = 0; index < state.list.length; index++) {
        const people = state.list[index];
        people.media = people.media.filter(f => f.id !== parseInt(action.payload));
      }
    }
  },
});

export const { saveCastListData, removeVideoFromPeople } = castSlice.actions;
export const selectCastList = state => state.cast.list;
export default castSlice.reducer;
