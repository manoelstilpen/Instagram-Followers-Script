package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

import java.util.ArrayList;
import java.util.List;

public class FeedPage extends BasePage {
    public FeedPage(WebDriver browser) {
        super(browser);

        try {
            Thread.currentThread().sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        // in case of notification popup appears: close it
        List<WebElement> notificationPopUp = browser.findElements(By.xpath("//button[@class='_dcj9f']"));
        if(notificationPopUp.size() > 0){
            notificationPopUp.get(0).click();
        }
    }

    public ProfilePage clickProfilePage(){

        browser.findElement(By.linkText("Perfil")).click();

        return new ProfilePage(browser);
    }
}
