package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class InitialPage extends BasePage {

    public InitialPage(WebDriver browser) {
        super(browser);
    }

    public InitialPage clickDoLogin(){
        browser.findElement(By.linkText("Faça login")).click();
        return this;
    }

    public InitialPage typeUsername(String username){
        browser.findElement(By.name("username")).sendKeys(username);
        return this;
    }

    public InitialPage typePassword(String password){
        browser.findElement(By.name("password")).sendKeys(password);
        return this;
    }


    public FeedPage clickLogin(){
        browser.findElement(By.xpath("//button[contains(.,'Entrar')]")).click();
        return new FeedPage(browser);
    }

    public FeedPage doLogin(String username, String passw){
        typeUsername(username);
        typePassword(passw);

        return clickLogin();
    }

}
