// import React from 'react';
import logo from './logo.svg';
import { useEffect, useState } from 'react';
import styles from './App.module.css'

interface PlayTurn {
  card_a_string: string,
  card_b_string: string,
  remaining_cards_a: number,
  remaining_cards_b: number,
  result: string,
  turn: number
}

interface Game {
  play_script: PlayTurn[]
  match_result: string
}

interface PlayerRecord {
  id: number,
  name: string,
  wins: number,
  losses: number,
  ties: number,
  updated_at: string,
  created_at: string
}
/*
  one page
  two inputs (player1 and player2)
  two decks represented
  flip top card
*/
function App() {

  const [player1, setPlayer1] = useState('')
  const [player2, setPlayer2] = useState('')
  const [playScript, setPlayScript] = useState<Game>()
  const [turnIndex, setTurnIndex] = useState(0)
  const [matchResult, setMatchResult] = useState('')
  const [tieCounter, setTieCounter] = useState(0)
  const [player1Record, setPlayer1Record] = useState<PlayerRecord>()
  const [player2Record, setPlayer2Record] = useState<PlayerRecord>()

 async function handleGetPlayScript(players: {player1: string, player2: string}) {
  try {
    const response = await fetch('http://localhost:5001/start-game', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(players)
    })
    if (response.ok) {
      const data = await response.json()
      setPlayScript(data)
    }
  } catch(e) {
    console.log(e)
  }
}

async function getPlayerRecord(player: string) {
  try {
    const response = await fetch('http://localhost:5001/all-time-record', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({player: player})
    })
    if (response.ok) {
      const data = await response.json()
      if (data.name === player1) setPlayer1Record(data)
      if (data.name === player2) setPlayer2Record(data)
    }
  } catch(e) {
    console.log(e)
  }
}
// async function animateTurn() {
//   setTurnIndex(turnIndex => {
//     // const currTurn = playScript.play_script[turnIndex]
//     if (turnIndex < playScript.play_script.length) setTimeout(animateTurn, 2000)
//     return turnIndex + 1
//   })
// }
//   const currTurn = playScript.play_script[turnIndex]

  // When the playscript is updated
  useEffect(() => {
    if (matchResult || playScript == null) { return }
    let turnIndex = 0

    const winCheck = () => {
      if (turnIndex > playScript.play_script.length) {
        return true
      } else {
        return false
      }
    }

    const interval = setInterval(() => {
      if (winCheck()) {
        setMatchResult(playScript.match_result)
      } else {
        setTurnIndex(turnIndex++)
      }
    }, 1000)

    return () => {
      clearInterval(interval)
    }
  }, [matchResult, playScript])
//
  const currTurn = playScript?.play_script[turnIndex]
  return (
    <div className={styles.App}>
      <h1>{ matchResult ? `WINNER IS ${matchResult}` : 'THIS IS WAR'}</h1>
      <div className={styles.arena}>
        <div className={styles.deck}>{currTurn ? currTurn.remaining_cards_a : null}</div>
        <div className={styles.drawcard}>{currTurn ? currTurn.card_a_string : null}</div>
        <div className={styles.line}></div>
        <div className={styles.drawcard}>{currTurn ? currTurn.card_b_string : null}</div>
        <div className={styles.deck}>{currTurn ? currTurn.remaining_cards_b : null}</div>
        {currTurn?.result === 'tie' &&<h1 className={styles.war}>{`WAR!`}</h1>}
      </div>
      <div className={styles.actions}>
        {!playScript && (
          <>
            <input className={styles.player_1} placeholder='player 1' onChange={e => setPlayer1(e.target.value.trim().toUpperCase())} value={player1}></input>
          </>
        )}
        {!playScript && (<>
          <input className={styles.player_2} placeholder='player 2' onChange={e => setPlayer2(e.target.value.trim().toUpperCase())} value={player2}></input>
        </>
        )}
        {!playScript && <button onClick={e => handleGetPlayScript({player1, player2})}>Play War</button>}
        {playScript && !matchResult && <button onClick={e => setMatchResult(playScript.match_result)}>Skip</button>}
        {matchResult && !player1Record && <button onClick={e => getPlayerRecord(player1)}>{`GET ${player1} RECORD`}</button>}
        {player1Record && (<div className={styles.record}>
          <div>{player1}</div>
          <div>{`WINS: ${player1Record.wins}`}</div>
          <div>{`LOSSES: ${player1Record.losses}`}</div>
          <div>{`TIES: ${player1Record.ties}`}</div>
        </div>)}
        {matchResult && <button onClick={e => {setMatchResult(''); setPlayScript(undefined); setPlayer1Record(undefined); setPlayer2Record(undefined)}}>Reset</button>}
        {matchResult && !player2Record  && <button onClick={e => getPlayerRecord(player2)}>{`GET ${player2} RECORD`}</button>}
        {player2Record && (<div className={styles.record}>
          <div>{player2}</div>
          <div>{`WINS: ${player2Record.wins}`}</div>
          <div>{`LOSSES: ${player2Record.losses}`}</div>
          <div>{`TIES: ${player2Record.ties}`}</div>
        </div>)}
      </div>
    </div>
  );
}
export default App;
