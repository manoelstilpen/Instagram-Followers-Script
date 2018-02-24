package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.util.ArrayList;
import java.util.List;

public class PopUp extends BasePage {

    protected WebElement popup;

    public PopUp(WebDriver browser) {
        super(browser);

        // focusing on popup
        popup = (new WebDriverWait(browser, 20))
                .until(ExpectedConditions.presenceOfElementLocated(
                        By.xpath("//div[contains(@class,'_gs38e')]")
                ));

        popup.click();
    }

    public List<String> getUsers(int nUsers){

        List<WebElement> userList = new ArrayList<WebElement>();
        while (userList.size() < nUsers){

            popup.sendKeys(Keys.PAGE_DOWN);
            popup.sendKeys(Keys.PAGE_DOWN);

            // returns a list with all users scrolled
            userList = browser.findElements(By.xpath("//ul[contains(@class,'_8q670')]//a[contains(@class,'_2g7d5')]"));

            try {
                Thread.currentThread().sleep(250);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            System.out.println(userList.size());
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
