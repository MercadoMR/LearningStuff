package mx.mimir.sproner.model;

import java.time.Duration;
import java.time.YearMonth;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

import com.vladmihalcea.hibernate.type.basic.YearMonthDateType;
import com.vladmihalcea.hibernate.type.interval.PostgreSQLIntervalType;

import org.hibernate.annotations.TypeDef;
/* https://thorben-janssen.com/key-jpa-hibernate-annotations/ */

@Entity
@Table(name="song", schema="music")
@TypeDef(
    typeClass = PostgreSQLIntervalType.class,
    defaultForType = Duration.class
)
@TypeDef(
    typeClass = YearMonthDateType.class,
    defaultForType = YearMonth.class
)
public class Song{
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private long id;

    @Column(name="title", nullable = false)
    private String title;

    @Column(name="description", columnDefinition="text")
    private String description;

    @Column(name="duration", columnDefinition="interval")
    private Duration duration;

    @Column(name="published_on", columnDefinition = "date")
    private YearMonth publishedOn;

    public Song(){

    }

    public Song(String title) {
        this.title = title;
    }

    public Song(String title, String description) {
        this.title = title;
        this.description = description;
    }

    public Song(String title, String description, Duration duration, YearMonth publishedOn) {
        this.title = title;
        this.description = description;
        this.duration = duration;
        this.publishedOn = publishedOn;
    }

    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public Duration getDuration() {
        return duration;
    }

    public void setDuration(Duration duration) {
        this.duration = duration;
    }

    public YearMonth getPublishedOn() {
        return publishedOn;
    }

    public void setPublishedOn(YearMonth publishedOn) {
        this.publishedOn = publishedOn;
    }
    
    @Override
    public String toString()
    {
        return "["+id+"] - Song name:"+ title 
        +"\n Description:"+ description
        +"\n Duration:"+ duration.toMinutes()
        +"\n Published on:"+ publishedOn.toString();
    }

}
