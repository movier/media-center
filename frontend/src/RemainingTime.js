import React from 'react';

class RemainingTime extends React.Component {
  constructor(props) {
    super(props);

    console.log('history state', props.location);
    const { remainingSeconds } = props.location.state;
    this.state = {
      remainingSeconds,
    };
    this.secondsToString = this.secondsToString.bind(this);
  }

  componentDidMount() {
    setInterval(() => {
      this.setState({ remainingSeconds: this.state.remainingSeconds - 1 })
    }, 1000);
  }

  secondsToString(seconds) {
    var numyears = Math.floor(seconds / 31536000);
    var numdays = Math.floor((seconds % 31536000) / 86400);
    var numhours = Math.floor(((seconds % 31536000) % 86400) / 3600);
    var numminutes = Math.floor((((seconds % 31536000) % 86400) % 3600) / 60);
    var numseconds = (((seconds % 31536000) % 86400) % 3600) % 60;
    return numyears + " years " + numdays + " days " + numhours + " hours " + numminutes + " minutes " + numseconds + " seconds";
  }

  render() {
    return <h1 style={{ color: 'white' }}>Remaining time: {this.secondsToString(this.state.remainingSeconds)} </h1>;
  }
}

export default RemainingTime;
