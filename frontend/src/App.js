import React from 'react';
import './App.css';

class App extends React.Component {

  constructor(props) {
    super(props);
    
    this.state = {
      data: [],
    };
  }

  componentDidMount() {
    fetch('/api').then(response => this.setState({ data: response.json() }));
  }

  render() {
    return (
      <div className="App">
        {this.state.data.map((value, index) => {
          return (
            <div key={index}>
              <img src={value.poster_uri} alt={value.title} />
              <p>{value.title}</p>
            </div>
          );
        })}
      </div>
    );
  }
}

export default App;
