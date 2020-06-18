import React from 'react';
import './App.css';

class VideoDetail extends React.Component {

  constructor(props) {
    super(props);

    console.log('dd', props.location.search);
    const searchParams = new URLSearchParams(props.location.search);
    this.state = {
      cast: searchParams.get('cast').split(','),
      newCast: '',
      start: '',
      end: '',
    };
  }

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

  handleShotButtonClicked = () => {
    fetch('/api/shots', {
      method: 'POST'
    }).then(() => {
      this.props.history.goBack()
    });
  }

  handleAddCastButtonClick = () => {
    if (!this.state.newCast) return;
    const searchParams = new URLSearchParams(this.props.location.search);
    const id = searchParams.get('id');
    const data = { cast_name: this.state.newCast };
    fetch(`/api/videos/${id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    }).then(() => {
      this.setState({ cast: this.state.cast.concat(this.state.newCast), newCast: '' });
    })
  }

  handleConfirmButtonClick = () => {
    if (!this.state.start || !this.state.end) return;
    const searchParams = new URLSearchParams(this.props.location.search);
    const input = searchParams.get('v');
    const [name, suffix]= input.split('.');
    const output = `${name}_copy.${suffix}`;
    const data = {
      input,
      output,
      start: this.state.start,
      end: this.state.end,
    };
    fetch('/api/ffmpeg', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    }).then(() => {
      console.log('done');
    });
  }

  render() {
    const searchParams = new URLSearchParams(this.props.location.search);
    return (
      <>
        <video controls autoPlay>
          <source src={searchParams.get('v')} />
        </video>
        <button onClick={this.handleDeleteButtonClicked}>Delete</button>
        <button onClick={this.handleShotButtonClicked}>Shot</button>
        <div>{this.state.cast.map((m, i) => <span style={{ marginRight: 10 }} key={i}>{m}</span>)}</div>
        <div>
          <span>New Cast:</span>
          <input type="text" value={this.state.newCast} onChange={e => this.setState({ newCast: e.target.value })} />
          <button onClick={this.handleAddCastButtonClick}>Add Cast</button>
        </div>
        <div>
          <span>Start:</span>
          <input type="text" value={this.state.start} onChange={e => this.setState({ start: e.target.value })} />
          <span>End:</span>
          <input type="text" value={this.state.end} onChange={e => this.setState({ end: e.target.value })} />
          <button onClick={this.handleConfirmButtonClick}>Confirm</button>
        </div>
      </>
    );
  }
}

export default VideoDetail;
