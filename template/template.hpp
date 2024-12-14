#ifndef TEMPLATE_HPP
#define TEMPLATE_HPP

#include <libdnf5-cli/session.hpp>
#include <string>

namespace dnf5 {

class TemplateCommand : public libdnf5::cli::session::Command {
public:
    explicit TemplateCommand(libdnf5::cli::session::Session & session);
    void run() override; // Function to execute the command
};

} // namespace dnf5

#endif // TEMPLATE_HPP
