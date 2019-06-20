import React from 'react';
import './VideoList.css';
import { Link } from "react-router-dom";

class VideoList extends React.Component {

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
    fetch('/api?is_check=true')
      .then(response => response.json())
      .then(data => {
        this.setState({ data });
      });
  }

  render() {
    return (
      <div className="VideoList">
        {this.state.data.map((value, index) => {
          return (
            <div key={index}>
              <Link className="VideoList__link" to={`/watch?v=${value.uri}`}>
                <img src={value.poster_uri} alt={value.title} />
                <p className="VideoList__title">{value.title}</p>
              </Link>
            </div>
          );
        })}
      </div>
    );
  }
}

export default VideoList;
