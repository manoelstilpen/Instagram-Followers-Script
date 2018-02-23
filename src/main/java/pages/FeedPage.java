package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class FeedPage extends BasePage {
    public FeedPage(WebDriver browser) {
        super(browser);
    }

    public ProfilePage clickProfilePage(){

        browser.findElement(By.linkText("Perfil")).click();

        return new ProfilePage(browser);
    }
}
