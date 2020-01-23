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
        if (data.has_error && data.error_code === 403) {
          console.log('error', data.error_message);
          const { remaining_seconds: remainingSeconds } = data.data;
          this.props.history.replace('/remaining-time', { remainingSeconds });
        } else {
          this.setState({ data });
        }
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
            const { uri, poster_uri, title, id, cast } = value;
            const castNames = cast.map(m => m.name).join(',');
            return (
              <div key={index}>
                <Link className="VideoList__link" to={`/watch?v=${uri}&id=${id}&cast=${castNames}`}>
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
