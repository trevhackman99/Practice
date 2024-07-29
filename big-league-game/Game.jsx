import React from 'react';
import startImg from '../images/baseball001.png';

function Game() {
  return (
    <body>
        <div className='title'>
        <h1>Game Loaded</h1>
        </div>

        <div className='game-ctn'>
            <div className='game-inner-ctn'>
                <img id='start-img' src={startImg} alt="Kids playing baseball" />
                <div className='game-options-ctn'>
                    <button>Start</button>
                    <button>TEMP</button>
                </div>
            </div>
        </div>
    </body>
  );
}

export default Game;