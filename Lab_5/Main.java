package Lab_5;
import java.util.ArrayList;

public class Main {
    
    public static void playAll(ArrayList<nexusMedia> media){
        for (nexusMedia medium : media){
            medium.play();
        }
    }

    public static void main(String[] args) {
        ArrayList<nexusMedia> media = new ArrayList<>();
        
        video video1 = new video(5.26, "Dog_goes_to_park.mp4", "720p");
        video video2 = new video(9.28, "Youtube_video_rough_draft.mp4", "1080p");
        audio audio1 = new audio(550.05, "Stacys_mom.mp3", "44.1kHz");
        audio audio2 = new audio(502.93, "Jump.wav", "44.1kHz");

        media.add(video1);
        media.add(video2);
        media.add(audio1);
        media.add(audio2);

        playAll(media);

        
    } 
}
