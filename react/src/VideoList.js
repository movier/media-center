import React from 'react';
import './VideoList.css';
import { Link } from "react-router-dom";

class VideoList extends React.Component {

  constructor(props) {
    super(props);
    
    this.state = {
      data: [],
      test: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
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
          <Link to="/cast">Cast</Link>
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
          {this.state.test.map(value => (
            <div key={value} style={{ width: '100%', height: 100, backgroundColor: 'cyan' }}>
              <Link className="VideoList__link" to={'/watch?v=/sample5.mp4&id=2&cast=Test2,TTTTT'}>List {value}</Link>
            </div>
          ))}
        </div>
      </div>
    );
  }
}

export default VideoList;
