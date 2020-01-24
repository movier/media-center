import React from 'react';
import './VideoList.css';
import { Link } from "react-router-dom";

class CastList extends React.Component {

  constructor(props) {
    super(props);
    
    this.state = {
      data: [],
    };
  }

  componentDidMount() {
    fetch('/api/cast')
      .then(response => response.json())
      .then(data => { 
        this.setState({ data });
      });
  }

  render() {
    return (
      <div>
        {this.state.data.map((cast, cast_index) => {
          const { name, videos } = cast;
          return (
            <div key={cast_index}>
              <div style={{ color: 'white' }}>{name}</div>
              <div className="VideoList">
                {videos.map((value, index) => {
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
        })}
      </div>
    );
  }
}

export default CastList;
