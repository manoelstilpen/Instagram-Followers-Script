package model;

import driver.LoadProfile;
import org.openqa.selenium.WebDriver;
import support.Web;

public class Main {

    public static void main(String[] args){

        Instagram user = new Instagram("manoelstilpen", "123456");

        WebDriver browser = Web.createChromeInstance();

        LoadProfile.load(browser, user);


    }
}
