package model;

import java.util.List;

public class Instagram {

    public String username;
    public String password;

    public int nFollowing;
    public int nFollowers;

    public List<String> following;
    public List<String> followers;

    public Instagram(String user, String passw) {
        init(user,passw);
    }

    public void init(String user, String passw){
        this.username = user;
        this.password = passw;
    }

}
