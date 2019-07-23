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
  }

  handleCheckUpdate = () => {
    fetch('/api?is_check=true')
      .then(response => response.json())
      .then(data => {
        this.setState({ data });
      });
  }

  render() {
    return (
      <div>
        <div style={{ marginTop: 16, textAlign: 'center' }}>
          <button onClick={this.handleCheckUpdate}>检查更新</button>
        </div>
        <div className="VideoList">
          {this.state.data.map((value, index) => {
            const { uri, poster_uri, title, id } = value;
            return (
              <div key={index}>
                <Link className="VideoList__link" to={`/watch?v=${uri}&id=${id}`}>
                  <img src={poster_uri} alt={title} />
                  <p className="VideoList__title">{title}</p>
                </Link>
              </div>
            );
          })}
        </div>
      </div>
    );
  }
}

export default VideoList;
