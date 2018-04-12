from connect import Connect
from tictactoe.Multiplayer.multi_gameplay import MultiplayerGameplay
from More_or_less.molgameplay import MoLGameplay

con1 = Connect()
con1.make_connection()

mode = con1.send_data("Choose game (mol - more or less OR ttt - Tic-Tac-Toe) :", True)
if not (mode == "ttt" or mode == "mol"):
	mode = con1.send_data("Choose game (mol - more or less OR ttt - Tic-Tac-Toe) :", True)

if mode == 'ttt':
    con2 = Connect()
    con2.make_connection()
    gameplay = MultiplayerGameplay(con1, con2)
    gameplay.start()
    con2.close_connection()
    con1.close_connection()

if mode == "mol":
    gameplay = MoLGameplay(con1)
    gameplay.start()
    con1.close_connection()

