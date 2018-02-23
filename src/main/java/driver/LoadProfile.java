package driver;

import model.Instagram;
import org.openqa.selenium.WebDriver;
import pages.InitialPage;

public class LoadProfile {

    /**
     * Loads the profile specified
     * @param profile an instagram profile
     * @return a populated instagram profile with Following and Followers
     */
    public static Instagram load(WebDriver browser, Instagram profile){

        new InitialPage(browser).clickDoLogin()
        .doLogin("manoelstilpen", "123456");

        return profile;
    }


}
