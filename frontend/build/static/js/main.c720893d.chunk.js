(window.webpackJsonp=window.webpackJsonp||[]).push([[0],{14:function(t,e,n){},15:function(t,e,n){},16:function(t,e,n){"use strict";n.r(e);var a=n(0),o=n.n(a),r=n(2),i=n.n(r),c=(n(14),n(3)),u=n(4),s=n(6),l=n(5),d=n(7),m=(n(15),function(t){function e(t){var n;return Object(c.a)(this,e),(n=Object(s.a)(this,Object(l.a)(e).call(this,t))).state={data:[]},n}return Object(d.a)(e,t),Object(u.a)(e,[{key:"componentDidMount",value:function(){var t=this;fetch("/api").then(function(e){return t.setState({data:e})})}},{key:"render",value:function(){return o.a.createElement("div",{className:"App"},this.state.data.map(function(t,e){return o.a.createElement("div",{key:e},o.a.createElement("img",{src:t.poster_uri,alt:t.title}),o.a.createElement("p",null,t.title))}))}}]),e}(o.a.Component));Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));i.a.render(o.a.createElement(m,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then(function(t){t.unregister()})},8:function(t,e,n){t.exports=n(16)}},[[8,1,2]]]);
//# sourceMappingURL=main.c720893d.chunk.js.map