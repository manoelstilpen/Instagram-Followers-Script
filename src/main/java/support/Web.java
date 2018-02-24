package support;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

import java.util.concurrent.TimeUnit;

public class Web {

    public static WebDriver createChromeInstance(){

        System.setProperty("webdriver.chrome.driver", Commons.chromeDriverPath);
        WebDriver navegador = new ChromeDriver();
        navegador.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);

        navegador.get(Commons.instagramUrl);

        return navegador;
    }

    public static WebDriver createFirefoxInstance(){

        System.setProperty("webdriver.firefox.driver", Commons.firefoxDriverPath);
        WebDriver navegador = new FirefoxDriver();
        navegador.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);

        navegador.get(Commons.instagramUrl);

        return navegador;

    }
}
