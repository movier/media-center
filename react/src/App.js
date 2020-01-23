import React from "react";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import VideoList from './VideoList';
import VideoDetail from './VideoDetail';
import RemainingTime from './RemainingTime';
import CastList from './CastList';

function BasicExample() {
  return (
    <Router>
      <div>
        <Route exact path="/" component={VideoList} />
        <Route path="/watch" component={VideoDetail} />
        <Route path="/topics" component={Topics} />
        <Route path="/remaining-time" component={RemainingTime} />
        <Route path="/cast" component={CastList} />
      </div>
    </Router>
  );
}

function About({ match }) {
  console.log('location', match);
  return (
    <div>
      <h2>About, { decodeURIComponent(match.params.path) }</h2>
    </div>
  );
}

function Topics({ match }) {
  return (
    <div>
      <h2>Topics</h2>
      <ul>
        <li>
          <Link to={`${match.url}/rendering`}>Rendering with React</Link>
        </li>
        <li>
          <Link to={`${match.url}/components`}>Components</Link>
        </li>
        <li>
          <Link to={`${match.url}/props-v-state`}>Props v. State</Link>
        </li>
      </ul>

      <Route path={`${match.path}/:topicId`} component={Topic} />
      <Route
        exact
        path={match.path}
        render={() => <h3>Please select a topic.</h3>}
      />
    </div>
  );
}

function Topic({ match }) {
  return (
    <div>
      <h3>{match.params.topicId}</h3>
    </div>
  );
}

export default BasicExample;
