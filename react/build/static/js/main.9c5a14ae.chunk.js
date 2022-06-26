(window.webpackJsonp=window.webpackJsonp||[]).push([[0],{29:function(e,t,a){e.exports=a(43)},34:function(e,t,a){},39:function(e,t,a){},41:function(e,t,a){},42:function(e,t,a){},43:function(e,t,a){"use strict";a.r(t);var n=a(0),i=a.n(n),c=a(14),o=a.n(c),r=(a(34),a(7)),l=a(8),s=a(5),m=a(12),u=Object(m.b)({name:"video",initialState:{list:[]},reducers:{saveVideoListData:function(e,t){var a=t.payload;console.log("original data",a);for(var n=window.innerWidth,i=a.map(function(e){return e.width||(e.width=1e3),e.height||(e.height=1e3),e}),c=0,o=i.length-1,r=0,l=0,s=0;s<i.length;s++){var m=i[s],u=m.width/m.height;l+=u;var d=m.width/m.height*250;if((r+=d)>=n){var h=n/(l-u),f=n/l;console.log("height1",s,h,f,l);var p=h-250,v=250-f;if(Math.abs(p)>Math.abs(v)){o=s;for(var E=c;E<=o;E++)i[E].display_height=f,i[E].display_width=i[E].width/i[E].height*f;c=s+1,r=0,l=0}else{o=s-1;for(var g=c;g<=o;g++)i[g].display_height=h,i[g].display_width=i[g].width/i[g].height*h;c=s,r=d,l=u}}}console.log("new data 1",i),e.list=i},removeVideo:function(e,t){e.list=e.list.filter(function(e){return e.id!==parseInt(t.payload)})}}}),d=u.actions,h=d.saveVideoListData,f=d.removeVideo,p=u.reducer,v=function(e){return e.video.list};a(39);var E=function(e){var t=e.media,a=t.uri,n=t.poster_uri,c=t.title,o=t.id,l=t.people,s=(t.created_at,t.size,t.datetime),m=t.duration,u=t.media_type,d=t.display_height,h=t.display_width,f=l.map(function(e){return e.name}).join(",");return i.a.createElement("div",null,i.a.createElement(r.b,{className:"VideoList__link",to:"/watch?v=".concat(a,"&id=").concat(o,"&cast=").concat(f)},i.a.createElement("div",{style:{position:"relative"}},i.a.createElement("img",{className:"media-cell-img",style:{display:"block",width:h,height:d},src:n,alt:c}),2==u&&i.a.createElement("div",{style:{display:"flex",alignItems:"center",position:"absolute",top:10,right:10,color:"white",fontSize:12,fontWeight:"bold"}},new Date(1e3*Math.ceil(m)).toISOString().substr(11,8),i.a.createElement("span",{style:{marginLeft:4},className:"material-symbols-outlined"},"play_circle")),i.a.createElement("div",{style:{position:"absolute",bottom:10,left:10,color:"white",fontSize:12,fontWeight:"bold"}},i.a.createElement("p",{className:"VideoList__title"},s.replace("T"," ").slice(0,16))))))};function g(e){var t=Object(s.c)(v),a=Object(s.b)();Object(n.useEffect)(function(){t.length>0||fetch("/api").then(function(e){return e.json()}).then(function(t){if(console.log("response",t),t.has_error&&403===t.error_code){console.log("error",t.error_message);var n=t.data.remaining_seconds;e.history.replace("/remaining-time",{remainingSeconds:n})}else a(h(t))})},[]);return i.a.createElement("div",null,i.a.createElement("div",{style:{margin:16,textAlign:"center"}},i.a.createElement("button",{onClick:function(){fetch("/api?is_check=true").then(function(e){return e.json()}).then(function(e){a(h(e))})}},"\u68c0\u67e5\u66f4\u65b0"),i.a.createElement(r.b,{to:"/cast"},"Cast")),i.a.createElement("div",{className:"MediaList"},t.map(function(e,t){return i.a.createElement(E,{key:t,media:e})})))}var b=a(10),y=(a(41),Object(m.b)({name:"cast",initialState:{list:[]},reducers:{saveCastListData:function(e,t){e.list=t.payload},removeVideoFromPeople:function(e,t){for(var a=0;a<e.list.length;a++){var n=e.list[a];n.media=n.media.filter(function(e){return e.id!==parseInt(t.payload)})}}}})),w=y.actions,j=w.saveCastListData,O=w.removeVideoFromPeople,S=function(e){return e.cast.list},_=y.reducer;a(42);function k(e){var t=new URLSearchParams(e.location.search),a=t.get("id"),c=Object(n.useState)(t.get("cast").split(",")),o=Object(b.a)(c,2),r=(o[0],o[1],Object(n.useState)("")),l=Object(b.a)(r,2),m=(l[0],l[1],Object(n.useState)("")),u=Object(b.a)(m,2),d=(u[0],u[1],Object(n.useState)("")),h=Object(b.a)(d,2),p=(h[0],h[1],Object(n.useState)(null)),v=Object(b.a)(p,2),E=v[0],g=v[1],y=Object(n.useRef)(null);Object(n.useEffect)(function(){fetch("/api/media/".concat(a)).then(function(e){return e.json()}).then(function(e){g(e)})},[]);var w=Object(s.b)();return E?i.a.createElement("div",{className:"media-container"},function(e){switch(e.media_type){case 1:return i.a.createElement("img",{className:"media",src:e.uri});case 2:return i.a.createElement("video",{ref:y,className:"media",controls:!0,autoPlay:!0},i.a.createElement("source",{src:e.uri}));default:return i.a.createElement("h1",null,"Unknown Media Type")}}(E),i.a.createElement("div",{className:"operation-container"},i.a.createElement("div",{className:"operation-container__inner"},i.a.createElement("div",{className:"icon-container",onClick:function(){e.history.goBack()}},i.a.createElement("span",{className:"material-symbols-outlined"},"arrow_back")),i.a.createElement("div",{className:"operation-container__inner__right"},i.a.createElement("div",{className:"icon-container",onClick:function(){var e=y.current.currentTime;fetch("/api/thumbnail/".concat(a),{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({time:e})}).then(function(){window.alert("Screenshot success!")}).catch(function(e){console.error(e)})}},i.a.createElement("span",{className:"material-symbols-outlined"},"screenshot")),i.a.createElement("div",{className:"icon-container",onClick:function(){window.confirm("Are you sure to delete this video?")&&fetch("/api/media/".concat(a),{method:"DELETE"}).then(function(){w(f(a)),w(O(a)),e.history.goBack()})}},i.a.createElement("span",{className:"material-symbols-outlined"},"delete")))))):null}var N=a(25),M=a(26),L=a(16),T=a(28),C=a(27),I=function(e){Object(T.a)(a,e);var t=Object(C.a)(a);function a(e){var n;Object(N.a)(this,a),n=t.call(this,e),console.log("history state",e.location);var i=e.location.state.remainingSeconds;return n.state={remainingSeconds:i},n.secondsToString=n.secondsToString.bind(Object(L.a)(n)),n}return Object(M.a)(a,[{key:"componentDidMount",value:function(){var e=this,t=setInterval(function(){0===e.state.remainingSeconds?(clearInterval(t),e.props.history.replace("/")):e.setState({remainingSeconds:e.state.remainingSeconds-1})},1e3)}},{key:"secondsToString",value:function(e){return Math.floor(e/31536e3)+" years "+Math.floor(e%31536e3/86400)+" days "+Math.floor(e%31536e3%86400/3600)+" hours "+Math.floor(e%31536e3%86400%3600/60)+" minutes "+e%31536e3%86400%3600%60+" seconds"}},{key:"render",value:function(){return i.a.createElement("h1",{style:{color:"white"}},"Remaining time: ",this.secondsToString(this.state.remainingSeconds)," ")}}]),a}(i.a.Component);function V(){var e=Object(s.c)(S),t=Object(s.b)();return Object(n.useEffect)(function(){e.length>0||fetch("/api/cast").then(function(e){return e.json()}).then(function(e){t(j(e))})},[]),i.a.createElement("div",null,e.map(function(e,t){var a=e.name,n=e.media;return i.a.createElement("div",{key:t},i.a.createElement("div",{style:{color:"white"}},a),i.a.createElement("div",{className:"MediaList"},n.map(function(e,t){return i.a.createElement(E,{key:t,media:e})})))}))}function D(e){var t=e.match;return i.a.createElement("div",null,i.a.createElement("h2",null,"Topics"),i.a.createElement("ul",null,i.a.createElement("li",null,i.a.createElement(r.b,{to:"".concat(t.url,"/rendering")},"Rendering with React")),i.a.createElement("li",null,i.a.createElement(r.b,{to:"".concat(t.url,"/components")},"Components")),i.a.createElement("li",null,i.a.createElement(r.b,{to:"".concat(t.url,"/props-v-state")},"Props v. State"))),i.a.createElement(l.a,{path:"".concat(t.path,"/:topicId"),component:P}),i.a.createElement(l.a,{exact:!0,path:t.path,render:function(){return i.a.createElement("h3",null,"Please select a topic.")}}))}function P(e){var t=e.match;return i.a.createElement("div",null,i.a.createElement("h3",null,t.params.topicId))}var x=function(){return i.a.createElement(r.a,null,i.a.createElement(l.a,{exact:!0,path:"/",component:g}),i.a.createElement(l.a,{path:"/watch",component:k}),i.a.createElement(l.a,{path:"/topics",component:D}),i.a.createElement(l.a,{path:"/remaining-time",component:I}),i.a.createElement(l.a,{path:"/cast",component:V}))},R=Object(m.a)({reducer:{video:p,cast:_}});Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));o.a.render(i.a.createElement(i.a.StrictMode,null,i.a.createElement(s.a,{store:R},i.a.createElement(x,null))),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then(function(e){e.unregister()}).catch(function(e){console.error(e.message)})}},[[29,1,2]]]);
//# sourceMappingURL=main.9c5a14ae.chunk.js.map