export function mediaListGroupByDate(data) {
  const originalData = data.slice();
  const groupByDate = [];
  let currentDate = null;
  for (let index = 0; index < originalData.length; index++) {
    const element = originalData[index];
    const datetime = element.datetime.slice(0, 10);
    if (currentDate !== datetime) {
      currentDate = datetime;
      groupByDate.push({ datetime, data: [element] });
    } else {
      const index = groupByDate.map(m => m.datetime).indexOf(datetime);
      groupByDate[index].data.push(element);
    }
  }
  const basicHeight = 250;
  const windowWidth = window.innerWidth;

  for (let index = 0; index < groupByDate.length; index++) {
    const e1 = groupByDate[index];
    const element = {...e1};
    const originalData = element.data;
    const newData = originalData.map(m => {
      const newM = {...m};
      if (!m.width) {
        newM.width = 1000;
      }
      if (!m.height) {
        newM.height = 1000;
      }
      return newM;
    });
    let rowStartAt = 0;
    let rowEndAt = newData.length - 1;
    let rowWidth = 0;
    let totalRatio = 0;
    for (let index = 0; index < newData.length; index++) {
      const element = {...newData[index]};
      const ratio = element.width / element.height;
      totalRatio += ratio;
      const width = element.width / element.height * basicHeight;
      rowWidth += width;
      if (rowWidth >= windowWidth) {
        // Calculate actual height
        const height1 = windowWidth / (totalRatio - ratio);
        const height2 = windowWidth / totalRatio;
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
      } else {
        element.display_height = basicHeight;
        element.display_width = 'auto';
      }
    }
    element.data = newData;
  }
  return groupByDate;
}
