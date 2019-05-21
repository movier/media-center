import React from 'react';
import './App.css';

function App() {
  const data = [];
  for (let index = 0; index < 103; index++) {
    data.push(index);
  }
  return (
    <div className="App">
      {data.map((value, index) => {
        return (
          <div key={index}>
            <img src="/images/placeholder.png" alt={index} />
            <p>This is description of the image</p>
          </div>
        );
      })}
    </div>
  );
}

export default App;
