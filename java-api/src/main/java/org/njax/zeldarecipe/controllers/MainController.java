package org.njax.zeldarecipe.controllers;

import org.apache.pulsar.client.api.*;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.concurrent.TimeUnit;
import java.util.stream.IntStream;

@RestController
@RequestMapping("")
public class MainController {

    @Value("${pulsar.protocol_url}")
    private String protocolUrl;

    @GetMapping
    public String home() {
        return "hihi yoooz";
    }

    @GetMapping("/write_pulsar")
    public String writePulsar() {
        String response = "";
        try {
            PulsarClient client = PulsarClient.builder()
                    .serviceUrl(protocolUrl)  // .serviceUrl("pulsar://localhost:6650")
                    .build();

            Producer<byte[]> producer = client.newProducer()
                    .topic("my-topic")
                    .compressionType(CompressionType.LZ4)
                    .create();

            producer.send("My message".getBytes());

            producer.close();
            client.close();

            response = "Message written to pulsar";
        } catch (PulsarClientException e) {
            response = "Message failed to write";

            e.printStackTrace();
        }

        return response;
    }

}
