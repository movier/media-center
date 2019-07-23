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

  handleDeleteButtonClicked = () => {
    if (window.confirm("Are you sure to delete this video?")) { 
      const searchParams = new URLSearchParams(this.props.location.search);
      const id = searchParams.get('id');
      fetch(`/api/videos/${id}`, {
        method: 'DELETE'
      }).then(() => {
        this.props.history.goBack();
      });
    }
  }

  render() {
    const searchParams = new URLSearchParams(this.props.location.search);
    return (
      <>
        <video controls autoPlay>
          <source src={searchParams.get('v')} />
        </video>
        <button onClick={this.handleDeleteButtonClicked}>Delete</button>
      </>
    );
  }
}

export default VideoDetail;
