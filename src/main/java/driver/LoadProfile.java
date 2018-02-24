package driver;

import model.Instagram;
import org.openqa.selenium.WebDriver;
import pages.FollowersPopUp;
import pages.InitialPage;
import pages.ProfilePage;

import java.util.List;

public class LoadProfile {

    /**
     * Loads the profile specified
     * @param profile an instagram profile
     * @return a populated instagram profile with Following and Followers
     */
    public static Instagram load(WebDriver browser, Instagram profile){

        ProfilePage page = new InitialPage(browser).clickDoLogin()
        .doLogin(profile.username, profile.password).clickProfilePage();

        profile.nFollowers = page.getNFollowers();
        profile.nFollowing = page.getNFollowing();

        FollowersPopUp popupFollowers = page.clickFollowersPopUp();
        List<String> followers = popupFollowers.getFollowers(profile.nFollowers);
        popupFollowers.closePopUp();

        return profile;
    }


}
