package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class ProfilePage extends BasePage {

    public ProfilePage(WebDriver browser) {
        super(browser);
    }

    public int getNFollowing(){
        return Integer.parseInt(browser.findElement
                (By.xpath("//a[contains(@href, 'followers')]/span[@class='_fd86t']")).getText());
    }

    public int getNFollowers(){
        return Integer.parseInt(browser.findElement
                (By.xpath("//a[contains(@href, 'following')]/span[@class='_fd86t']")).getText());
    }


}
