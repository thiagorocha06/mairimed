/**
 *  SCRIPT
 */
// Here set the minutes, seconds, and tenths-of-second when you want the chronometer to stop
// If all these values are set to 0, the chronometer not stop automatically
var stmints = 0;
var stseconds = 0;
// selectors to elements, where we are displaying timer. They also are form fields, so they are going to be send to server
var mints_elm = document.getElementById('minutes')
var seconds_elm = document.getElementById('seconds')

// the initial tenths-of-second, seconds, and minutes
var seconds = 0;
var mints = 0;

var startchron = 0;

function chronometer() {
  if (startchron == 1) {
    seconds += 1; // set tenths of a second

    // set minutes
    if (seconds > 59) {
      seconds = 0;
      mints += 1;
    }

    // adds data in proper fields
    mints_elm.value = mints
    seconds_elm.value = seconds

    // if the chronometer reaches to the values for stop, calls whenChrStop(), else, auto-calls chronometer()
    if (seconds == stseconds && mints == stmints) {
      toAutoStop();
    } else {
      setTimeout("chronometer()", 1000);
     }
  }
}

function startChr() {
  startchron = 1;
  chronometer();
} // starts the chronometer
function stopChr() {
  startchron = 0;
} // stops the chronometer
function resetChr() {
  seconds = 0;
  mints = 0;
  startchron = 0;
  mints_elm.value = mints
  seconds_elm.value = seconds
}

/**
 *  HTML
 <form id="form" action="#urltobackendservice">
   <input name="minutes" id="minutes" value="0" type="text" /> :
   <input name="seconds" id="seconds" value="0" type="text" />
   <input type="submit" value="Send result" />
 </form>
 <hr />
 <button onclick="startChr()">Start the chronometer </button>
 <button onclick="stopChr()">Stop the chronometer</button>
 <button onclick="resetChr()">Reset the chronometer</button>
 */
/**
* CSS
input[type="text"] {
  font-size:21px;
  font-weight:800;
  width: 50px;
  text-align: center;
  border: none;
  background: transparent;
}
*/
