package pages;

import org.openqa.selenium.*;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.util.ArrayList;
import java.util.List;

public class FollowersPopUp extends BasePage {

    private WebElement popup;

    public FollowersPopUp(WebDriver browser) {
        super(browser);

        // focusing on popup
        popup = (new WebDriverWait(browser, 10))
                .until(ExpectedConditions.presenceOfElementLocated(
                        By.xpath("//div[contains(@class,'_gs38e')]")
                ));

        popup.click();

    }

    public List<String> getFollowers(int nFollowers){

        List<WebElement> userList = new ArrayList<WebElement>();
        while (userList.size() < nFollowers){

            popup.sendKeys(Keys.PAGE_DOWN);
            popup.sendKeys(Keys.PAGE_DOWN);

            // returns a list with all users scrolled
            userList = browser.findElements(By.xpath("//div[@class='_p4iax']//a[contains(@class,'_2g7d5')]"));

            try {
                Thread.currentThread().sleep(250);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        // converting WebElement to String
        List<String> list = new ArrayList<String>();
        for(WebElement e : userList){
            list.add(e.getText());
        }

        return list;
    }

    public ProfilePage closePopUp(){
        popup.sendKeys(Keys.ESCAPE);

        return new ProfilePage(browser);
    }


}
