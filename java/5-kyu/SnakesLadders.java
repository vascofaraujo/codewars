public class SnakesLadders {
    int player1 = 0;
    int player2 = 0;
    int currPlayer = 1;
    int gameOver = 0;
    public SnakesLadders() {
        this.player1 = player1;
        this.player2 = player2;
        this.currPlayer = currPlayer;
        this.gameOver = gameOver;
    }
    public String play(int die1, int die2) {
        int move = die1 + die2;
        int currPlayerNum = this.currPlayer;
        int currPlayerMove = 0;
        // int currPlayer = this.currPlayer;
        // int player1 = this.player1;
        // int player2 = this.player2;
        // int gameOver = this.gameOver;

        if (this.currPlayer == 1){
            this.player1 = this.player1 + move;
            currPlayerMove = this.player1;
        }else{
            this.player2 = this.player2 + move;
            currPlayerMove = this.player2;
        }

        if (die1 == die2){

            this.currPlayer = (this.currPlayer==1 ? 1 : 2);
        }else{
            this.currPlayer = (this.currPlayer==1 ? 2 : 1);
        }

        if (this.gameOver != 0 && currPlayerNum !=this.gameOver){
          this.player1 = 0;
          this.player2 = 0;
          this.gameOver = 0;
          return "Game over!";
        }
      if (currPlayerMove > 100){
            currPlayerMove = 100 - (currPlayerMove-100);
        }
        if (currPlayerMove == 2){
            currPlayerMove = 38;
        }else if (currPlayerMove == 7){
            currPlayerMove = 14;
        }else if (currPlayerMove == 8){
            currPlayerMove = 31;
        }else if (currPlayerMove == 15){
            currPlayerMove = 26;
        }else if (currPlayerMove == 16){
            currPlayerMove = 6;
        }else if (currPlayerMove == 21){
            currPlayerMove = 42;
        }else if (currPlayerMove == 28){
            currPlayerMove = 84;
        }else if (currPlayerMove == 36){
            currPlayerMove = 44;
        }else if (currPlayerMove == 46){
            currPlayerMove = 25;
        }else if (currPlayerMove == 49){
            currPlayerMove = 11;
        }else if (currPlayerMove == 51){
            currPlayerMove = 67;
        }else if (currPlayerMove == 62){
            currPlayerMove = 19;
        }else if (currPlayerMove == 64){
            currPlayerMove = 60;
        }else if (currPlayerMove == 71){
            currPlayerMove = 91;
        }else if (currPlayerMove == 74){
            currPlayerMove = 53;
        }else if (currPlayerMove == 78){
            currPlayerMove = 98;
        }else if (currPlayerMove == 87){
            currPlayerMove = 94;
        }else if (currPlayerMove == 89){
            currPlayerMove = 68;
        }else if (currPlayerMove == 92){
            currPlayerMove = 88;
        }else if (currPlayerMove == 95){
            currPlayerMove = 75;
        }else if (currPlayerMove == 99){
            currPlayerMove = 80;
        }else if (currPlayerMove == 100){
            this.gameOver = currPlayerNum;
            return "Player " + String.valueOf(currPlayerNum) + " Wins!";
        }

        if (currPlayerNum == 1){
            this.player1 = currPlayerMove;
        }else{
            this.player2 = currPlayerMove;
        }


        return "Player " + String.valueOf(currPlayerNum) + " is on square " + String.valueOf(currPlayerMove);
    }

    public static void main(String[] args) {
        SnakesLadders game = new SnakesLadders();
        System.out.println(game.play(99,1));
        System.out.println(game.play(4,3));
        System.out.println(game.play(2,2));
        System.out.println("New Game\n\n");
        SnakesLadders game2 = new SnakesLadders();
        System.out.println(game2.play(3,2));
        System.out.println(game2.play(2,2));
        System.out.println(game2.play(1,2));
    }
}
