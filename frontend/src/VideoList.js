import React from 'react';
import './App.css';
import { Link } from "react-router-dom";

class App extends React.Component {

  constructor(props) {
    super(props);
    
    this.state = {
      data: [],
    };
  }

  componentDidMount() {
    fetch('/api')
      .then(response => response.json())
      .then(data => { 
        console.log('response', data);
        this.setState({ data });
      });
  }

  render() {
    return (
      <div className="App">
        {this.state.data.map((value, index) => {
          return (
            <div key={index}>
              <Link to={`/watch?v=${value.uri}`}>
                <img src={value.poster_uri} alt={value.title} />
                <p>{value.title}</p>
              </Link>
            </div>
          );
        })}
      </div>
    );
  }
}

export default App;
