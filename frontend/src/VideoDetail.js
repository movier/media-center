import React from 'react';
import './App.css';

class VideoDetail extends React.Component {

  constructor(props) {
    super(props);

    console.log('dd', props.location.search);
    const searchParams = new URLSearchParams(props.location.search);
    console.log('video detail', searchParams.get('v'));
  }

  // componentDidMount() {
  //   fetch('/api')
  //     .then(response => response.json())
  //     .then(data => { 
  //       console.log('response', data);
  //       this.setState({ data });
  //     });
  // }

  render() {
    const searchParams = new URLSearchParams(this.props.location.search);
    return (
      <>
        <video controls autoPlay>
          <source src={searchParams.get('v')} />
        </video>
      </>
    );
  }
}

export default VideoDetail;
