package driver;

import model.Instagram;
import org.openqa.selenium.WebDriver;
import pages.*;

import java.util.List;

public class LoadProfile {

    /**
     * Loads the profile specified
     * @param profile an instagram profile
     * @return a populated instagram profile with Following and Followers
     */
    public static Instagram load(WebDriver browser, Instagram profile){

        ProfilePage profilePage = new InitialPage(browser)
                .doLogin(profile.username, profile.password).clickProfilePage();

        profile.nFollowers = profilePage.getNFollowers();
        profile.nFollowing = profilePage.getNFollowing();

        PopUp popupFollowers = profilePage.clickFollowersPopUp();
        List<String> followers = popupFollowers.getUsers(profile.nFollowers);
        popupFollowers.closePopUp();

        PopUp popupFollowing = profilePage.clickFollowingPopUp();
        List<String> following = popupFollowing.getUsers(profile.nFollowing);
        popupFollowing.closePopUp();

        profile.followers = followers;
        profile.following = following;

        return profile;
    }


}
