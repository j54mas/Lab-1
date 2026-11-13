package Lab_5;

public class video extends nexusMedia {

    protected String resolution;

    public video(double fileSize, String title, String resolution){
        super(fileSize, title);

        this.resolution = resolution; 

    }

    @Override
    public void play(){
       System.out.println("Rendering frames at " + this.resolution);

    }

}

