import java.util.Random;
import java.util.Scanner;

public class practice12 {
    public static void main(String[] args) {
        System.out.println("Welcome to Rock:Paper:Sessior Game");
        System.out.println("enter 0 : ROCK \t1:PAPER\t 2:SESSOIR");
        Scanner sc=new Scanner(System.in);
        Random rd=new Random();
        int n=1;
        int count=0;
        while(n<=3){
            System.out.println("Your turn enter number");
            int user_input=sc.nextInt();
            switch(user_input){
                case 0:
                { System.out.println("You select Rock");
                }break;

                case 1:{System.out.println("You select Paper");
                }break;
                case 2:
                {
                    System.out.println("You select Sessior");
                }break;
            }
            System.out.println("Computer's turn ");
            int comp_input=rd.nextInt(3);
            switch(comp_input){
                case 0:
                { System.out.println("Computer select Rock");
                }break;

                case 1: {
                    System.out.println("Computer select Paper");
                }break;
                case 2:{
                    System.out.println("Computer select Sessior");
                }break;
            }
            if(user_input==comp_input){
                System.out.println("Draw match");
            }
            else if((user_input==0&& comp_input==2)||(user_input==1 && comp_input==0)||(user_input==2 && comp_input==1))
            {
                System.out.println("Congratulations! You win the match");
                count++;
            }
            else {
                System.out.println("You not win,Better luck next time");
            }

            n++;

        }
        System.out.println("you won mathes "+count+ "times");




    }
}