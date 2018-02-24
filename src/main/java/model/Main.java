package model;

import driver.LoadProfile;
import driver.NotFollowBack;
import org.openqa.selenium.WebDriver;
import support.Web;

import java.util.List;

public class Main {

    public static void main(String[] args){

        Instagram user = new Instagram("user", "passw");

        WebDriver browser = Web.createFirefoxInstance();

        user = LoadProfile.load(browser, user);

        List<String> notFollowBack = NotFollowBack.doesNotFollowMeBack(user);

        for(String i : notFollowBack){
            System.out.println(i);
        }

    }
}
