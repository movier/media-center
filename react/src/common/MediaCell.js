import React from 'react';
import { Link } from "react-router-dom";

/**
 * Format bytes as human-readable text.
 * 
 * @param bytes Number of bytes.
 * @param si True to use metric (SI) units, aka powers of 1000. False to use 
 *           binary (IEC), aka powers of 1024.
 * @param dp Number of decimal places to display.
 * 
 * @return Formatted string.
 */
 function humanFileSize(bytes, si=false, dp=1) {
  const thresh = si ? 1000 : 1024;

  if (Math.abs(bytes) < thresh) {
    return bytes + ' B';
  }

  const units = si 
    ? ['kB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'] 
    : ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB'];
  let u = -1;
  const r = 10**dp;

  do {
    bytes /= thresh;
    ++u;
  } while (Math.round(Math.abs(bytes) * r) / r >= thresh && u < units.length - 1);


  return bytes.toFixed(dp) + ' ' + units[u];
}

export default function ({ media }) {
  const { uri, poster_uri, title, id, people, created_at, size, datetime, duration } = media;
  const peopleNames = people.map(m => m.name).join(',');
  return (
    <div>
      <Link className="VideoList__link" to={`/watch?v=${uri}&id=${id}&cast=${peopleNames}`}>
        <img src={poster_uri} alt={title} />
        <p className="VideoList__title">{title}</p>
        <p className="VideoList__title">{created_at}</p>
        <p className="VideoList__title">{humanFileSize(size, true)}</p>
        <p className="VideoList__title">{datetime}</p>
        <p className="VideoList__title">{new Date(Math.ceil(duration) * 1000).toISOString().substr(11, 8)}</p>
      </Link>
    </div>
  );
}