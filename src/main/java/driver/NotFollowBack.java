package driver;

import model.Instagram;
import org.openqa.selenium.WebDriver;

import java.util.ArrayList;
import java.util.List;

public class NotFollowBack {

    public static List<String> doesNotFollowMeBack(Instagram user){

        List<String> notFollowBack = new ArrayList<String>();

        for(String following : user.following){
            Boolean followMe = false;
            for(String follower : user.followers){
                if(following.contains(follower)){
                    followMe = true;
                    break;
                }
            }

            if(!followMe){
                notFollowBack.add(following);
            }
        }

        return notFollowBack;
    }
}
